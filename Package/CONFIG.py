import ops
import ops_git
import iopc

TARBALL_FILE="LuaJIT-2.0.5.tar.gz"
TARBALL_DIR="LuaJIT-2.0.5"
TARBALL_TARGET="lua-bin"
pkg_path = ""
output_dir = ""
tarball_pkg = ""
tarball_dir = ""
install_dir = ""

#make HOST_CC="gcc -m32" CROSS=arm-linux-gnueabi- TARGET_CFLAGS="-mfloat-abi=soft"
def set_global(args):
    global pkg_path
    global output_dir
    global tarball_pkg
    global install_dir
    global tarball_dir
    global PHPROOT
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    pkg_args = args["pkg_args"]
    tarball_pkg = ops.path_join(pkg_path, TARBALL_FILE)
    tarball_dir = ops.path_join(output_dir, TARBALL_DIR)
    install_dir = ops.path_join(output_dir, TARBALL_TARGET)

def MAIN_ENV(args):
    set_global(args)

    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.unTarXz(tarball_pkg, output_dir)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(tarball_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return True

def MAIN_BUILD(args):
    set_global(args)

    crosscc=ops.getEnv("CROSS_COMPILE")
    extrac_config = ['HOST_CC="gcc -m32"', 'TARGET_CFLAGS="-mfloat-abi=soft"', 'CROSS=' + crosscc, 'PREFIX=' + install_dir ]
    iopc.make(tarball_dir, extrac_config)

    return False

def MAIN_INSTALL(args):
    set_global(args)

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)

