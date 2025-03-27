#!/bin/bash

# Strict mode: exit on error, undefined variable, or pipe failure
set -euo pipefail

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration variables
PROJECT_NAME="duckdb-query-project"
DOCKER_IMAGE="datacatering/duckdb:v1.2.1"
DB_VOLUME_PATH="./db"
PYTHON_VERSION="3"

# Logging function
log() {
    echo -e "${GREEN}[SETUP]${NC} $1"
}

# Error handling function
error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
    exit 1
}

# Prerequisite checks
check_prerequisites() {
    log "Checking system prerequisites..."
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        error "Docker is not installed. Please install Docker first."
    fi
    
    # Check Python
    if ! command -v python${PYTHON_VERSION} &> /dev/null; then
        error "Python ${PYTHON_VERSION} is not installed."
    fi
    
    # Check pip
    if ! command -v pip &> /dev/null; then
        error "pip is not installed. Please install pip for Python ${PYTHON_VERSION}."
    fi
}

# Create virtual environment
setup_python_env() {
    log "Setting up Python virtual environment..."
    # python${PYTHON_VERSION} -m venv venv
    # source venv/bin/activate
    
    # Install dependencies
    pip install --upgrade pip
    pip install -r requirements.txt
    #pip install -e .
}

# Setup Docker volume and configuration
setup_docker_env() {
    log "Preparing Docker environment..."
    
    
    # Create database volume directory if not exists
    rm -rf ${DB_VOLUME_PATH}
    mkdir -p ${DB_VOLUME_PATH}
    
    # Pull Docker image
    docker pull ${DOCKER_IMAGE}
    
    # Create Docker network (optional, for future expansion)
    docker network create ${PROJECT_NAME}_network || true
}

# Initialize database
initialize_database() {
    log "Initializing database..."
    
    # docker run -it --rm \
    docker rm -f duckdb_server
    docker run -itd \
        -v $(pwd)/${DB_VOLUME_PATH}:/db \
        --name duckdb_server \
        ${DOCKER_IMAGE}

    cp database/6a8ba9d16583414f9abce56141502022_0.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_1.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_2.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_3.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_4.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_5.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_6.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_7.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_8.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_9.parquet db/
    cp database/6a8ba9d16583414f9abce56141502022_9.parquet db/
    cp database/init.sql db/
    docker exec -it duckdb_server sh -c "/duckdb /db/vehicle_data.db < /db/init.sql"
    docker exec -it duckdb_server sh -c "chmod 777 /db/vehicle_data.db"
}

# Main setup function
main() {
    check_prerequisites
    setup_python_env
    setup_docker_env
    initialize_database
    
    log "Setup completed successfully!"
    #log "Activate virtual environment with: source venv/bin/activate"
}

# Run main setup
main




# Variable to track overall test success
TESTS_PASSED=true

# Directory containing test files
TEST_DIR="tests"

# Run each Python test file
for test_file in ${TEST_DIR}/*.py; do
    echo "Running test: $test_file"
    
    # Run the test and capture the exit code
    if python3 "$test_file"; then
        echo "✅ $test_file PASSED"
    else
        echo "❌ $test_file FAILED"
        TESTS_PASSED=false
    fi
done

# Determine final exit code based on test results
if [ "$TESTS_PASSED" = true ]; then
    echo "All tests passed successfully! 🎉"
    exit 0
else
    echo "Some tests failed. Please review test results. ❌"
    exit 1
fi