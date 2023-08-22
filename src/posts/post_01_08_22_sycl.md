# Sycl setup for Linux and macOS
1 aug 2022 (Updated 22 aug 2023)

In this post I'm describing how to get DPCPP & OpenSYCL working.


## DPCPP (Linux only)

- clone the repo : 

```sh
git clone https://github.com/intel/llvm -b sycl
```

- to configure : 

```sh
python3 buildbot/configure.py --llvm-external-projects compiler-rt --cmake-opt="-DCMAKE_INSTALL_PREFIX=../../sycl_cpl/dpcpp"
```

or if cuda is available

```sh
cd llvm
python3 buildbot/configure.py --llvm-external-projects compiler-rt --cuda --cmake-opt="-DCMAKE_INSTALL_PREFIX=../../sycl_cpl/dpcpp"
```

- to compile : 

```sh
python3 buildbot/compile.py
```
or (in build directory)
```sh
ninja all
```


<br/>

## OpenSYCL (Linux / Macos)

- to clone : 
```sh
git clone --recurse-submodules https://github.com/OpenSYCL/OpenSYCL
```
- to configure : 
```sh
cd hipSYCL
cmake -DCMAKE_INSTALL_PREFIX=../../sycl_cpl/OpenSYCL .
```
- to compile / install: 
```sh
make -j install
```

<br/>

## Helper script

Will clone, configure, compile everything in the working directory. When finished compiler are available in the sycl_cpl folder.

```sh
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    #CYGWIN*)    machine=Cygwin;;
    #MINGW*)     machine=MinGw;;
    #*)          machine="UNKNOWN:${unameOut}"
esac
echo "type : ${machine}"



mkdir -p sycl_cpl_src


if [ ! "$machine" == "Mac" ]
then 
    mkdir -p sycl_cpl_src/dpcpp
fi

mkdir -p sycl_cpl/hipSYCL

if [ ! "$machine" == "Mac" ]
then 
    mkdir -p sycl_cpl/dpcpp
    cd sycl_cpl_src/dpcpp

    echo "$(pwd)"


    if [ -d "llvm" ] 
    then
        echo "dpcpp folder found -> git pull"
        cd llvm 
        git pull
        cd ..
    else
        echo "dpcpp folder not found -> git clone"
        git clone https://github.com/intel/llvm -b sycl
    fi

    cd ../..

fi


cd sycl_cpl_src

if [ -d "hipSYCL" ] 
then
    echo "hipSYCL folder found -> git pull"
    cd hipSYCL 
    git pull
    cd ..
else
    echo "hipSYCL folder not found -> git clone"
    git clone --recurse-submodules https://github.com/OpenSYCL/OpenSYCL
fi

cd ..



echo "$(pwd)"

echo "compiling OpenSYCL"
cd sycl_cpl_src/OpenSYCL
cmake -DCMAKE_INSTALL_PREFIX=../../sycl_cpl/OpenSYCL .
make -j install
cd ..

if [ ! "$machine" == "Mac" ]
then 
    echo "compiling dpcpp"
    cd dpcpp/llvm
    echo "$(pwd)"

    if ! type "$nvcc" > /dev/null; then
        echo "CUDA=false"
        python3 buildbot/configure.py --llvm-external-projects compiler-rt --cmake-opt="-DCMAKE_INSTALL_PREFIX=../../sycl_cpl/dpcpp"
    else
        echo "CUDA=true"
        python3 buildbot/configure.py --llvm-external-projects compiler-rt --cuda --cmake-opt="-DCMAKE_INSTALL_PREFIX=../../sycl_cpl/dpcpp"
    fi

    cd build
    ninja all

fi
```

<br/>

## Getting the autocompletion working with clangd

If you're using cmake add in CMakeLists.txt :
```cmake
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

A file named ```compile_commands.json``` will appear in your build directory. Clangd can read this file to know to compilations steps & flags. But clangd doesn't know any SyCL compiler flag nor any SyCL includes. To solve that you can create a .clangd file in the root directory of your project.

```
CompileFlags:
  Remove: [ -fsycl, -fsycl-targets=*, --hipsycl-targets=*, --hipsycl-platform=*, --hipsycl-config-file=*,--hipsycl-cpu-cxx=*]
  Add: []
```