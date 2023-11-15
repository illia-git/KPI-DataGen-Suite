# KPI DataGen Suite

## Overview
KPI DataGen Suite is a comprehensive Python tool designed to generate random but structured datasets of Key Performance Indicators (KPIs). Initially created during a contract with Efigence (Artegence) for internal purposes, this tool played a crucial role in preparing visualizations for Looker Studio using hypothetical data. The task involved defining KPIs for a popular car brand's website. To enhance the realism and practicality of the data used in these visualizations, I developed this tool to work with actual CSV files generated based on predefined KPIs, rather than relying solely on imaginary data. The project is tailored for analytics and testing purposes, offering a quick way to create realistic KPI data. It follows clean code principles and is structured to facilitate easy maintenance and scalability.

## Features
- **Modular Data Generation**: Separately handle the generation of date and KPI data, promoting code reusability and clarity.
- **Comprehensive KPI List**: Includes a wide range of KPIs such as Total Visits, Bounce Rate, Conversion Rate, and more, catering to diverse analytical needs.
- **CSV Export Functionality**: Easily export generated data to CSV format, making it convenient to use in various data analysis tools.
- **Unit Testing**: Comes with a set of unit tests ensuring the reliability of the data generation logic and file operations.
- **Clean Code Practice**: Written with readability and maintainability in mind, adhering to the clean code principles and Google's Python style guide.

## Installation
Clone the repository to your local machine:
```bash
  git clone https://github.com/illia-git/KPI-DataGen-Suite
```

## Usage
Navigate to the project directory and run the main script:
```bash
  python main.py
```

This will generate a CSV file with random KPI data based on predefined settings.

## Project Structure
- `main.py`: The entry point of the application.
- `data_generation/`: Modules for generating date and KPI data.
- `utils/`: Utility functions, including CSV export functionality.
- `tests/`: Unit tests for the various modules.

## Contributing
Contributions to the KPI DataGen Suite are welcome. Please ensure that all pull requests adhere to the existing coding standards and include relevant unit tests.
