from .server import serve

def main():
    """MCP Shell Server - Execute shell commands through MCP"""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="give a model the ability to execute shell commands"
    )

    args = parser.parse_args()
    asyncio.run(serve())


if __name__ == "__main__":
    main() 