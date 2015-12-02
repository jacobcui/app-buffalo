CLOSURE_LIBRARY_DIR=../../closure-library
CLOSURE_COMPILER_DIR=../../closure-compiler
CLOSURE_COMPILER=${CLOSURE_COMPILER_DIR}/compiler.jar
CLOSURE_TEMPLATES_DIR=../../closure-templates
CLOSURE_TEMPLATES_COMPILER_DIR=../../closure-templates-compiler

# Soy compiler
CLOSURE_TEMPLATES_COMPILER=${CLOSURE_TEMPLATES_COMPILER_DIR}/SoyToJsSrcCompiler.jar
CLOSURE_SOY_UTILS=${CLOSURE_TEMPLATES_DIR}/javascript/soyutils_usegoog.js
CLOSURE_DEPS_JS = ${CLOSURE_LIBRARY_DIR}/closure/goog/deps.js
CLOSURE_JS=$(shell find ${CLOSURE_LIBRARY_DIR} -name '*.js' | awk '{print "--js " $$1;}' -)
CLOSURE_TEMPLATE_JS=$(shell find ${CLOSURE_TEMPLATES_JS_DIR} -name '*.js' | awk '{print "--js " $$1;}' -)

# Dependency calculator
CALC_DEPS=${CLOSURE_LIBRARY_DIR}/closure/bin/calcdeps.py

OBJS=app.soy.js app.js cloud.js
DEPS_OBJS=-i app.soy.js -i app.js -i cloud.js -i ${CLOSURE_SOY_UTILS}
COMPILED_JS=app.min.js
DEP_JS = deps.js

%.soy.js: %.soy
	java -jar $(CLOSURE_TEMPLATES_COMPILER) \
	--outputPathFormat $@ \
	--shouldGenerateJsdoc \
	--shouldProvideRequireSoyNamespaces \
	$^

all: ${COMPILED_JS}

# Using the Dependency Calculation Script
# https://developers.google.com/closure/library/docs/calcdeps?hl=en
dep_js: $(COMPILED_JS)
	python $(CALC_DEPS) $(DEPS_OBJS) -p $(CLOSURE_LIBRARY_DIR)/closure/ \
	-o deps -c $(CLOSURE_COMPILER) > $(DEP_JS)

${COMPILED_JS}: ${OBJS} ${CLOSURE_SOY_UTILS}

# Using closurecompiler
# Available compilation levels:
#    WHITESPACE_ONLY
#    SIMPLE_OPTIMIZATIONS
#    ADVANCED_OPTIMIZATIONS
#
	java -jar ${CLOSURE_COMPILER} \
	--compilation_level=WHITESPACE_ONLY \
	--manage_closure_dependencies true \
	$(CLOSURE_SOY_UTILS) $(CLOSURE_JS) $^ \
	--closure_entry_point=app \
	> $@

.PHONY: clean

clean:
	rm *.soy.js ${COMPILED_JS} ${DEP_JS}
