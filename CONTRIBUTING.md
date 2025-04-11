# Contributing to KANUGA AI

Thank you for your interest in contributing to KANUGA AI! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## How to Contribute

1. **Fork the Repository**: Start by forking the repository to your GitHub account.
2. **Clone Your Fork**: Clone your fork to your local machine.
   ```bash
   git clone https://github.com/your-username/kanuga-ai.git
   cd kanuga-ai
   ```
3. **Create a Branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make Changes**: Make your changes, following the coding standards below.
5. **Test Your Changes**: Ensure your changes work as expected and don't break existing functionality.
6. **Commit Your Changes**: Commit your changes with a clear and descriptive commit message.
   ```bash
   git commit -m "Add feature: your feature description"
   ```
7. **Push to Your Fork**: Push your changes to your fork on GitHub.
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Create a Pull Request**: Create a pull request from your fork to the main repository.

## Coding Standards

- **Python**: Follow PEP 8 guidelines for Python code.
- **JavaScript/TypeScript**: Follow the ESLint configuration in the project.
- **Documentation**: Keep documentation up-to-date with your changes.
- **Tests**: Write tests for new features and ensure all tests pass.

## Development Setup

1. Set up the development environment using the provided scripts:
   ```bash
   python setup_local.py
   ```

2. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

3. Start the development servers:
   - Backend: `uvicorn backend.main:app --reload`
   - Frontend: `cd frontend && npm start`

## Reporting Issues

- Use the GitHub issue tracker to report bugs or request features.
- Provide detailed information about the issue, including steps to reproduce.

## License

By contributing to KANUGA AI, you agree that your contributions will be licensed under the project's MIT License. 