# UUID4 MCP Server

UUIDバージョン4を生成するMCPサーバー。

## 機能

このMCPサーバーは以下のツールを提供します：

- `generate_uuid4`: パラメータなしでUUID4を生成して返します
- `generate_multiple_uuid4`: 指定した数のUUID4を生成して返します

## インストール方法

1. 依存関係のインストール

```bash
uv sync
```

2. MCPの設定ファイルに追加

```json
{
  "mcpServers": {
    "uuid-server": {
      "command": "python",
      "args": ["-m", "uuid_server.main"],
      "disabled": false,
      "alwaysAllow": []
    }
  }
}
```

## 使用例

```
<use_mcp_tool>
<server_name>uuid-server</server_name>
<tool_name>generate_uuid4</tool_name>
<arguments>
{}
</arguments>
</use_mcp_tool>
```

または

```
<use_mcp_tool>
<server_name>uuid-server</server_name>
<tool_name>generate_multiple_uuid4</tool_name>
<arguments>
{
  "count": 5
}
</arguments>
</use_mcp_tool>
