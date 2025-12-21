from mssql.base import DatabaseWrapper

# Add support for SQL Server 2025 (v17)
DatabaseWrapper._sql_server_versions[17] = 2025
