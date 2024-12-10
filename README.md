# PoC Source Generator

This project is a Proof of Concept (PoC) for creating a .NET Source Generator. Source Generators are a powerful feature in the .NET ecosystem, allowing developers to generate additional source code at compile time to simplify and enhance development workflows. This PoC demonstrates basic functionality and serves as a foundation for more advanced implementations.

For a detailed introduction to C# Source Generators, check out this excellent [blog article](https://medium.com/c-sharp-programming/mastering-at-source-generators-18125a5f3fca).

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing. This guide will also include notes on deploying the project in a live system.

## Useful Links

- [Blog: Mastering at Source Generators](https://medium.com/c-sharp-programming/mastering-at-source-generators-18125a5f3fca)
- [Microsoft Documentation on Source Generators](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview)
- [Roslyn GitHub Repository](https://github.com/dotnet/roslyn)

### Prerequisites

Before running the project, ensure you have the following tools installed:

- [.NET SDK 6.0 or later](https://dotnet.microsoft.com/download)
- [Visual Studio 2022](https://visualstudio.microsoft.com/) (with the ".NET Desktop Development" workload installed)
- Basic knowledge of C# and Roslyn APIs (optional but recommended)

### Installing

Follow these steps to set up the development environment:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/poc-source-generator.git
   cd poc-source-generator
   ```

2. **Open the Solution**

   Open the `PoCSourceGenerator.sln` file in Visual Studio 2022.

3. **Build the Project**

   Build the solution to restore NuGet packages and ensure all dependencies are installed.

   ```bash
   dotnet build
   ```

4. **Run the Demo Project**

   - The solution includes a demo project where the Source Generator is applied. Run the demo project to see the generated code in action.
   - Open the `Generated` folder (or the Output window) in Visual Studio to inspect the generated files.

### Using the Source Generator

1. Add a reference to the Source Generator project in your main application.
2. Annotate your code with attributes defined in the Source Generator.
3. Build your solution to trigger code generation.
4. Review the generated code in the `obj` folder of your project.

### Example

Here is an example of using the Source Generator:

#### Input Code:

```csharp
[AutoGenerate]
public partial class ExampleClass
{
    public string Name { get; set; }
}
```

#### Generated Code:

```csharp
public partial class ExampleClass
{
    public string GeneratedProperty => $"Hello, {Name}!";
}
```

### Notes

- Generated files are located in the `obj` directory by default.
- Use the diagnostic tools in Visual Studio to troubleshoot issues related to code generation.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
