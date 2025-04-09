#!/usr/bin/env python3
import uuid

from mcp.server.fastmcp import Context, FastMCP

app = FastMCP()


@app.tool()
async def generate_uuid4(ctx: Context) -> str:
    """Generate and return a UUID4"""
    generated_uuid = str(uuid.uuid4())
    return generated_uuid


@app.tool()
async def generate_multiple_uuid4(ctx: Context, count: int = 1) -> list[str]:
    """Generate and return multiple UUID4s"""
    if count < 1 or count > 100:
        raise ValueError("count must be an integer between 1 and 100")

    generated_uuids = [str(uuid.uuid4()) for _ in range(count)]
    return generated_uuids


def main() -> None:
    """Main function"""
    app.run()


if __name__ == "__main__":
    main()
