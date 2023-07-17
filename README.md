# nvcc4jupyter

This is an adaptation of the nvcc4jupyter plugin at https://github.com/frehseg/nvcc4jupyter

## How to install or uninstall

- Install via remote repo

    ```
    pip install git+https://github.com/0400H/nvcc4jupyter
    ```

- Install via local repo

    ```
    git clone https://github.com/0400H/nvcc4jupyter
    cd nvcc4jupyter
    python ./setup.py install
    cd -
    ```

- Uninstal

    ```
    pip uninstall NVCCPlugin
    ```

## How to add compiler flags

Programmer can add `compiler flags` to `compiler_flags` in [nvcc_plugin.py](nvcc_plugin.py).
