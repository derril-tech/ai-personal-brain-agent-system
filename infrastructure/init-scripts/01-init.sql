-- MindMesh Database Initialization Script
-- This script sets up the PostgreSQL database with pgvector extension

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create database if it doesn't exist
-- Note: This should be run as a superuser
-- CREATE DATABASE mindmesh;

-- Connect to the mindmesh database
-- \c mindmesh;

-- Create custom types
CREATE TYPE autonomy_level AS ENUM ('L0', 'L1', 'L2', 'L3');
CREATE TYPE goal_status AS ENUM ('pending', 'running', 'completed', 'failed');
CREATE TYPE run_status AS ENUM ('running', 'completed', 'failed', 'paused');
CREATE TYPE approval_state AS ENUM ('pending', 'approved', 'rejected');
CREATE TYPE connector_status AS ENUM ('active', 'inactive', 'error');
CREATE TYPE document_sensitivity AS ENUM ('public', 'private', 'confidential');

-- Create indexes for better performance
-- These will be created automatically by SQLAlchemy, but we can add custom ones here

-- Create a function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create a function for vector similarity search
CREATE OR REPLACE FUNCTION vector_similarity(a vector, b vector)
RETURNS float
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN 1 - (a <=> b);
END;
$$;

-- Create a function for semantic search
CREATE OR REPLACE FUNCTION semantic_search(
    query_embedding vector(1536),
    match_threshold float,
    match_count int
)
RETURNS TABLE (
    id int,
    content text,
    similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        documents.id,
        documents.content,
        1 - (documents.vector <=> query_embedding) as similarity
    FROM documents
    WHERE 1 - (documents.vector <=> query_embedding) > match_threshold
    ORDER BY documents.vector <=> query_embedding
    LIMIT match_count;
END;
$$;

-- Grant necessary permissions
-- GRANT ALL PRIVILEGES ON DATABASE mindmesh TO mindmesh_user;
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mindmesh_user;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mindmesh_user;
-- GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO mindmesh_user;

-- Create a view for recent activity
CREATE OR REPLACE VIEW recent_activity AS
SELECT 
    'goal' as type,
    id,
    text as title,
    status,
    created_at,
    updated_at
FROM goals
UNION ALL
SELECT 
    'run' as type,
    id,
    'Run ' || id as title,
    status,
    created_at,
    updated_at
FROM runs
ORDER BY updated_at DESC;

-- Create a view for memory summary
CREATE OR REPLACE VIEW memory_summary AS
SELECT 
    'documents' as memory_type,
    COUNT(*) as count,
    COUNT(*) FILTER (WHERE is_indexed = true) as indexed_count
FROM documents
UNION ALL
SELECT 
    'episodes' as memory_type,
    COUNT(*) as count,
    COUNT(*) as indexed_count
FROM episodes
UNION ALL
SELECT 
    'entities' as memory_type,
    COUNT(*) as count,
    COUNT(*) as indexed_count
FROM entities;

-- Add comments for documentation
COMMENT ON DATABASE mindmesh IS 'MindMesh Personal Brain Agent System Database';
COMMENT ON EXTENSION vector IS 'pgvector extension for vector similarity search';
COMMENT ON FUNCTION semantic_search IS 'Function for semantic search using vector embeddings';
COMMENT ON VIEW recent_activity IS 'View showing recent activity across goals and runs';
COMMENT ON VIEW memory_summary IS 'View showing summary of memory storage';
