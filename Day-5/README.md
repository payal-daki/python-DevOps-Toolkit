
```markdown
# Day-5 | Command Line Args & Env Vars

## Command Line Arguments

Command line arguments allow you to pass inputs to a Python script when executing it from the terminal. They are accessed using `sys.argv` or libraries like `argparse`.

### Key Points:
- 🛠️ **Usage**: Command line arguments are useful for passing parameters dynamically when invoking scripts.
- 🔒 **Security Concerns**: Avoid passing sensitive information like passwords directly as command line arguments, especially in CI/CD or automation scripts.
- 📝 **Example**: If you run `python script.py my_password`, `my_password` will be visible in plain text and can be exposed if scripts are accessed by unauthorized users.

### Best Practices:
- **Avoid Hardcoding**: Instead of hardcoding sensitive data, consider using environment variables for secure storage and access.
- **Validation**: Validate and sanitize command line inputs to prevent errors and potential security vulnerabilities.

## Environment Variables

Environment variables provide a secure way to store sensitive data and configuration settings outside of your codebase.

### Key Points:
- 🌐 **Usage**: Preferred method for managing sensitive information in CI/CD pipelines, Docker containers, and server configurations.
- 🛡️ **Security**: Environment variables keep sensitive data hidden from source code and version control systems.
- 🚀 **Example**: Set an environment variable `PASSWORD` and access it securely in Python using `os.getenv('PASSWORD')`.

### Implementation:
1. **Setting Environment Variables**:
   - **Linux/macOS**: Use `export` command: `export PASSWORD=my_secret`.
   - **Windows**: Use System Properties > Environment Variables or PowerShell: `$env:PASSWORD="my_secret"`.

2. **Accessing in Python**:
   ```python
   import os

   password = os.getenv('PASSWORD')
   if password:
       print(f"Password retrieved: {password}")
   else:
       print("Password not found.")
   ```

## Summary

Understanding how to effectively use command line arguments and environment variables is crucial for securely managing sensitive information in your Python projects. By following best practices and using these methods appropriately, you can enhance the security and flexibility of your applications.

### Practice Exercise

Implement a Python script that utilizes both command line arguments and environment variables. Ensure sensitive data is handled securely and follow the discussed best practices.
```

