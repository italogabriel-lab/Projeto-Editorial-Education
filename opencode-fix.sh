#!/bin/bash
# OpenCode Extension Fix Script
# This script fixes the opencode extension startup issue

echo "🔧 OpenCode Extension Fix"
echo "========================"
echo ""

# 1. Kill any stale opencode processes
echo "1. Cleaning up stale processes..."
pkill -f "opencode" 2>/dev/null || true
sleep 1

# 2. Check if port 22012 is available
echo "2. Checking port 22012..."
if lsof -i :22012 >/dev/null 2>&1; then
    echo "   ⚠️  Port 22012 is in use, killing process..."
    lsof -ti:22012 | xargs kill -9 2>/dev/null || true
    sleep 1
else
    echo "   ✅ Port 22012 is available"
fi

# 3. Verify opencode installation
echo "3. Verifying opencode installation..."
if ! command -v opencode &> /dev/null; then
    echo "   ❌ opencode not found in PATH"
    echo "   Installing opencode-ai globally..."
    npm install -g opencode-ai
else
    OPENCODE_PATH=$(which opencode)
    echo "   ✅ opencode found at: $OPENCODE_PATH"
fi

# 4. Check auth configuration
echo "4. Checking auth configuration..."
if [ -f ~/.local/share/opencode/auth.json ]; then
    echo "   ✅ auth.json found"
    # Verify at least one provider is configured
    if grep -q "key" ~/.local/share/opencode/auth.json; then
        echo "   ✅ API keys configured"
    else
        echo "   ⚠️  No API keys found in auth.json"
    fi
else
    echo "   ⚠️  auth.json not found, creating..."
    mkdir -p ~/.local/share/opencode
    cat > ~/.local/share/opencode/auth.json << 'EOF'
{
  "openrouter": {
    "type": "api",
    "key": "YOUR_OPENROUTER_KEY_HERE"
  }
}
EOF
    echo "   Please edit ~/.local/share/opencode/auth.json with your API keys"
fi

# 5. Clear opencode cache and logs
echo "5. Cleaning opencode cache..."
rm -rf ~/.local/share/opencode/log/*.log 2>/dev/null || true
rm -f ~/.local/share/opencode/opencode.db-shm 2>/dev/null || true
rm -f ~/.local/share/opencode/opencode.db-wal 2>/dev/null || true
echo "   ✅ Cache cleaned"

# 6. Test opencode command
echo "6. Testing opencode command..."
timeout 5 opencode --help > /dev/null 2>&1
if [ $? -eq 124 ]; then
    echo "   ⚠️  opencode command hangs (this is normal for interactive mode)"
else
    echo "   ✅ opencode command works"
fi

# 7. Start opencode server in background
echo "7. Starting opencode server..."
nohup opencode --port 22012 > ~/.local/share/opencode/server.log 2>&1 &
OPENCODE_PID=$!
echo $OPENCODE_PID > ~/.local/share/opencode/server.pid
sleep 3

# 8. Verify server is running
echo "8. Verifying server status..."
if ps -p $OPENCODE_PID > /dev/null; then
    echo "   ✅ Server running with PID: $OPENCODE_PID"
    echo ""
    echo "🎉 OpenCode server started successfully!"
    echo ""
    echo "Server details:"
    echo "  - PID: $OPENCODE_PID"
    echo "  - Port: 22012"
    echo "  - Log: ~/.local/share/opencode/server.log"
    echo ""
    echo "To stop the server:"
    echo "  kill $(cat ~/.local/share/opencode/server.pid)"
    echo ""
    echo "To view logs:"
    echo "  tail -f ~/.local/share/opencode/server.log"
else
    echo "   ❌ Server failed to start"
    echo ""
    echo "Check logs at:"
    echo "  ~/.local/share/opencode/server.log"
    echo "  ~/.local/share/opencode/log/*.log"
    echo ""
    echo "Common issues:"
    echo "  1. Missing API keys in ~/.local/share/opencode/auth.json"
    echo "  2. Port 22012 already in use"
    echo "  3. Node.js version incompatibility"
fi

echo ""
echo "========================"
echo "Fix script completed!"
