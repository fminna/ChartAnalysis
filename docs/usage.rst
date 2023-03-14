Usage
=====

This section provides information on how to use this project.

Command-Line Interface
----------------------

This project includes a command-line interface (CLI) that can be used to perform various tasks.

The CLI is accessed by running the `myapp` command from a terminal or command prompt.

Here is an examples of how to use the CLI::

    myapp -h


Docker
----------------------

This project can also be run as a Docker container.

Here are the commands needed to run it as a container:

1. Build the project image::    
    
    docker build -t my-python-project .

2. Run the container::

    docker run my-python-project -h
