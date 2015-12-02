COMPILER=${HOME}
SOY_COMPILER=${HOME}/closure-templates/SoyToJsSrcCompiler.jar
CLOSURE_COMPILER=${HOME}/closure-compiler
CLOSURE_TEMPLATES=${HOME}/closure-templates
SUBDIRS=assets

subdirs:
	for dir in $(SUBDIRS); do \
        $(MAKE) -C $$dir; \
        done

.PHONY: subdirs $(SUBIRS)

$(SUBDIRS):
	$(MAKE) -C $@

compile:
	@java -jar compiler/compiler.jar \
	--compilation_level=ADVANCED_OPTIMIZATIONS \
	--only_closure_dependencies \
	$(CLOSURE_JS) $(SAMPLE_JS) $(CLOSURE_TEMPLATE_JS) \
	--closure_entry_point=sample.app \
	> min/sample-min.js


%.soy:
	echo $COMPILER
	java -jar $(SOY_COMPILER) \
	--outputPathFormat assets/$${d}.soy.js \
	--shouldGenerateJsdoc \
	--shouldProvideRequireSoyNamespaces \
	assets/$${d}.soy; \


all:
	echo ${COMPILER}
