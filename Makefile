all: RPMS/noarch/php-mediawiki-tuleap-123-1.23.9-6.noarch.rpm

SOURCES/mediawiki-1.23.9.tar.gz:
	mkdir -p SOURCES
	tar -czf SOURCES/mediawiki-1.23.9.tar.gz mediawiki-1.23.9

RPMS/noarch/php-mediawiki-tuleap-123-1.23.9-6.noarch.rpm: SOURCES/mediawiki-1.23.9.tar.gz
	rpmbuild --define "%_topdir $(CURDIR)" -bb php-mediawiki-tuleap.spec

clean:
	rm -rf BUILD BUILDROOT RPMS SOURCES SPECS SRPMS
