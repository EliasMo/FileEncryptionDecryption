# FileEncryptionDecryption
Create a simple tool that allow users to encrypt and decrypt files using a secure algorithm. This project will involve file handling, encryption and possibly a command-line interface(CLI).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


## Introduction

This tool provides a basic implementation of file encryption and decryption using the Advanced Encryption Standard (AES) algorithm. It can be useful for securing sensitive files.

## Features

- AES encryption and decryption
- Command-line interface for easy use

## Getting Started

### Prerequisites

- Python 3

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd FileEncryptionDecryption

    Install dependencies:

    bash

    pip install -r requirements.txt

Usage

Encrypt a file:

bash

python3 encrypt.py --file input.txt --output encrypted.txt

Decrypt a file:

bash

python3 decrypt.py --file encrypted.txt --output decrypted.txt
