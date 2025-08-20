#!/bin/bash

# =============================================================================
# MindMesh - Personal Brain Agent System
# Development Environment Setup Script
# =============================================================================

set -e  # Exit on any error

echo "🧠 Setting up MindMesh Development Environment..."
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required tools are installed
check_requirements() {
    print_status "Checking system requirements..."
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3.11+ is required but not installed."
        exit 1
    fi
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        print_error "Node.js 18+ is required but not installed."
        exit 1
    fi
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        print_error "Docker is required but not installed."
        exit 1
    fi
    
    # Check Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is required but not installed."
        exit 1
    fi
    
    print_success "All system requirements met!"
}

# Setup environment file
setup_environment() {
    print_status "Setting up environment configuration..."
    
    if [ ! -f .env ]; then
        cp env.example .env
        print_success "Created .env file from template"
        print_warning "Please edit .env file with your configuration"
    else
        print_warning ".env file already exists, skipping..."
    fi
}

# Start infrastructure services
start_infrastructure() {
    print_status "Starting infrastructure services..."
    
    # Start PostgreSQL and Redis
    docker-compose up -d postgres redis
    
    # Wait for services to be ready
    print_status "Waiting for services to be ready..."
    sleep 10
    
    # Check if services are running
    if docker-compose ps | grep -q "Up"; then
        print_success "Infrastructure services started successfully!"
    else
        print_error "Failed to start infrastructure services"
        exit 1
    fi
}

# Setup backend
setup_backend() {
    print_status "Setting up Python backend..."
    
    cd backend
    
    # Create virtual environment
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        print_success "Created Python virtual environment"
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install dependencies
    pip install -r requirements.txt
    
    # Run database migrations
    print_status "Running database migrations..."
    alembic upgrade head
    
    print_success "Backend setup completed!"
    cd ..
}

# Setup frontend
setup_frontend() {
    print_status "Setting up Next.js frontend..."
    
    cd frontend
    
    # Install dependencies
    npm install
    
    print_success "Frontend setup completed!"
    cd ..
}

# Setup AI engine
setup_ai_engine() {
    print_status "Setting up AI engine..."
    
    cd ai_engine
    
    # Create virtual environment
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        print_success "Created AI engine virtual environment"
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt
    
    print_success "AI engine setup completed!"
    cd ..
}

# Create necessary directories
create_directories() {
    print_status "Creating necessary directories..."
    
    mkdir -p logs
    mkdir -p data
    mkdir -p uploads
    mkdir -p temp
    
    print_success "Directories created!"
}

# Setup development tools
setup_dev_tools() {
    print_status "Setting up development tools..."
    
    # Install pre-commit hooks if available
    if command -v pre-commit &> /dev/null; then
        pre-commit install
        print_success "Pre-commit hooks installed"
    else
        print_warning "pre-commit not found, skipping hooks installation"
    fi
    
    print_success "Development tools setup completed!"
}

# Health check
health_check() {
    print_status "Running health check..."
    
    # Check if services are responding
    if curl -f http://localhost:5432 > /dev/null 2>&1; then
        print_success "PostgreSQL is responding"
    else
        print_warning "PostgreSQL health check failed"
    fi
    
    if curl -f http://localhost:6379 > /dev/null 2>&1; then
        print_success "Redis is responding"
    else
        print_warning "Redis health check failed"
    fi
    
    print_success "Health check completed!"
}

# Main setup function
main() {
    echo "Starting MindMesh setup..."
    echo ""
    
    check_requirements
    setup_environment
    start_infrastructure
    setup_backend
    setup_frontend
    setup_ai_engine
    create_directories
    setup_dev_tools
    health_check
    
    echo ""
    echo "🎉 MindMesh setup completed successfully!"
    echo ""
    echo "Next steps:"
    echo "1. Edit .env file with your configuration"
    echo "2. Start the backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
    echo "3. Start the frontend: cd frontend && npm run dev"
    echo "4. Visit http://localhost:3000 to access the application"
    echo ""
    echo "For more information, see the README.md file."
}

# Run main function
main "$@"
