#!/bin/bash
function check_git {
    GIT_VERSION=`git --version`
    if [ "$?" != "0" ]; then
	echo "Please instal git first."
	exit
    fi
}
check_git

INSTALL_DIR=$(dirname `pwd`)

CLOSURE_LIBRARY=closure-library
CLOSURE_TEMPLATES=closure-templates
CLOSURE_TEMPLATES_COMPILER=closure-templates-compiler
CLOSURE_TEMPLATES_COMPILER_FILE=closure-templates-for-javascript-latest.zip
CLOSURE_COMPILER=closure-compiler
CLOSURE_LINTER=closure-linter
    
function install_closure_lib {
    ## Get closure-library
    git clone https://github.com/google/${CLOSURE_LIBRARY}.git ${INSTALL_DIR}/${CLOSURE_LIBRARY}
}

function install_closure_templates {
    ## Get closure-templates
    git clone https://github.com/google/closure-templates.git ${INSTALL_DIR}/${CLOSURE_TEMPLATES}
    curl -O https://dl.google.com/closure-templates/${CLOSURE_TEMPLATES_COMPILER_FILE}
    ## Get closure-template-compiler. SoyToJsSrcCompiler.jar.
    unzip ${CLOSURE_TEMPLATES_COMPILER_FILE} -d ${CLOSURE_TEMPLATES_COMPILER}
    mv ${CLOSURE_TEMPLATES_COMPILER_FILE} ${CLOSURE_TEMPLATES_COMPILER} ${INSTALL_DIR}/
}

function install_closure_compiler {
    mkdir ${CLOSURE_COMPILER}
    curl -O https://dl.google.com/closure-compiler/compiler-latest.zip && unzip compiler-latest.zip -d ${CLOSURE_COMPILER}
    mv ${CLOSURE_COMPILER} ${INSTALL_DIR}/
}

function install_closure_linter {
    git clone https://github.com/google/${CLOSURE_LINTER}.git ${INSTALL_DIR}/${CLOSURE_LINTER}
    sudo python ${INSTALL_DIR}/${CLOSURE_LINTER}/setup.py install
    PWD=`pwd`
    cd ${INSTALL_DIR}/${CLOSURE_LINTER}
    sudo python setup.py install
    cd $PWD
    # After installing, you get two helper applications installed into /usr/local/bin:
    # gjslint - runs the linter and checks for errors
    # fixjsstyle - tries to fix errors automatically
}

case $1 in
    *)
        install_closure_lib ;
        install_closure_compiler ;
        install_closure_templates ;
        install_closure_linter ;;
esac
