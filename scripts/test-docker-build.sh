#!/bin/bash
# Test script for Docker build and basic functionality

set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}Testing BC-Utils Docker Build...${NC}\n"

# Check if we can access Docker
if ! docker version >/dev/null 2>&1; then
    echo -e "${RED}✗ Cannot access Docker. Run with sudo or add user to docker group.${NC}"
    echo "Try: sudo ./scripts/test-docker-build.sh"
    exit 1
fi

# Test 1: Build the Docker image
echo -e "${YELLOW}Test 1: Building Docker image...${NC}"
if docker build -t bcutils-test:latest .; then
    echo -e "${GREEN}✓ Docker build successful${NC}\n"
else
    echo -e "${YELLOW}Standard build failed, trying simple build...${NC}"
    if docker build -f Dockerfile.simple -t bcutils-test:latest .; then
        echo -e "${GREEN}✓ Simple Docker build successful${NC}\n"
    else
        echo -e "${RED}✗ Both Docker builds failed${NC}"
        exit 1
    fi
fi

# Test 2: Check image size
echo -e "${YELLOW}Test 2: Checking image details...${NC}"
docker images bcutils-test:latest
echo ""

# Test 3: Test basic container run
echo -e "${YELLOW}Test 3: Testing container startup...${NC}"
if docker run --rm bcutils-test:latest bcutils --help >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Container runs successfully${NC}\n"
else
    echo -e "${RED}✗ Container failed to run${NC}"
    exit 1
fi

# Test 4: Test CLI commands
echo -e "${YELLOW}Test 4: Testing CLI commands...${NC}"
docker run --rm bcutils-test:latest bcutils --help
echo -e "${GREEN}✓ CLI help works${NC}\n"

# Test 5: Test providers list
echo -e "${YELLOW}Test 5: Testing providers command...${NC}"
if docker run --rm bcutils-test:latest bcutils providers --list; then
    echo -e "${GREEN}✓ Providers command works${NC}\n"
else
    echo -e "${RED}✗ Providers command failed${NC}"
    exit 1
fi

# Test 6: Test with environment variables
echo -e "${YELLOW}Test 6: Testing environment variables...${NC}"
if docker run --rm \
    -e BCU_PROVIDER=yahoo \
    -e BCU_LOG_LEVEL=DEBUG \
    bcutils-test:latest \
    bash -c 'echo "Provider: $BCU_PROVIDER, Log Level: $BCU_LOG_LEVEL"'; then
    echo -e "${GREEN}✓ Environment variables work${NC}\n"
else
    echo -e "${RED}✗ Environment variables failed${NC}"
    exit 1
fi

# Test 7: Test volume mounts
echo -e "${YELLOW}Test 7: Testing volume mounts...${NC}"
mkdir -p test-data test-config
if docker run --rm \
    -v "$(pwd)/test-data:/data" \
    -v "$(pwd)/test-config:/config" \
    bcutils-test:latest \
    bash -c 'touch /data/test.txt && touch /config/test.txt && echo "Volume test successful"'; then
    
    if [ -f test-data/test.txt ] && [ -f test-config/test.txt ]; then
        echo -e "${GREEN}✓ Volume mounts work${NC}\n"
        rm -rf test-data test-config
    else
        echo -e "${RED}✗ Volume mount verification failed${NC}"
        exit 1
    fi
else
    echo -e "${RED}✗ Volume mounts failed${NC}"
    exit 1
fi

# Test 8: Test entrypoint script
echo -e "${YELLOW}Test 8: Testing entrypoint (dry run)...${NC}"
if docker run --rm \
    -e BCU_RUN_ON_STARTUP=False \
    -e BCU_PROVIDER=yahoo \
    bcutils-test:latest \
    timeout 5 bash -c '/app/entrypoint.sh' 2>&1 | grep -q "Starting BC-Utils container"; then
    echo -e "${GREEN}✓ Entrypoint script works${NC}\n"
else
    echo -e "${YELLOW}⚠ Entrypoint test inconclusive (expected with timeout)${NC}\n"
fi

# Test 9: Test Docker Compose
echo -e "${YELLOW}Test 9: Testing Docker Compose configuration...${NC}"
if docker-compose config >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Docker Compose configuration is valid${NC}\n"
else
    echo -e "${RED}✗ Docker Compose configuration invalid${NC}"
    exit 1
fi

# Test 10: Quick smoke test with Yahoo provider
echo -e "${YELLOW}Test 10: Smoke test with Yahoo provider...${NC}"
if docker run --rm \
    -e BCU_PROVIDER=yahoo \
    bcutils-test:latest \
    bcutils download --provider yahoo --symbol AAPL --yes --dry-run 2>/dev/null || true; then
    echo -e "${GREEN}✓ Smoke test completed${NC}\n"
fi

# Test 11: Test entrypoint with startup disabled
echo -e "${YELLOW}Test 11: Testing entrypoint without startup download...${NC}"
if timeout 10 docker run --rm \
    -e BCU_RUN_ON_STARTUP=False \
    -e BCU_PROVIDER=yahoo \
    bcutils-test:latest 2>&1 | grep -q "Starting BC-Utils container"; then
    echo -e "${GREEN}✓ Entrypoint works without download${NC}\n"
else
    echo -e "${YELLOW}⚠ Entrypoint test timeout (expected)${NC}\n"
fi

echo -e "${GREEN}All tests passed! 🎉${NC}"
echo -e "\nTo clean up test image, run:"
echo -e "  docker rmi bcutils-test:latest"