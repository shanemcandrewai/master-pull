""" git pull a series of repositories """
import subprocess as sp
print(sp.run(["git", "-C", "../../vimfiles", "pull"], capture_output=True, check=True))
print(sp.run(["git", "-C", "../build_libtorch", "pull"], capture_output=True, check=True))
print(sp.run(["git", "-C", "../aten_min", "pull"], capture_output=True, check=True))
print(sp.run(["git", "-C", "../aten_libtorch", "pull"], capture_output=True, check=True))
print(sp.run(["git", "-C", "../libtorch_subdir", "pull"], capture_output=True, check=True))
