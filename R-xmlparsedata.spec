#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xmlparsedata
Version  : 1.0.5
Release  : 16
URL      : https://cran.r-project.org/src/contrib/xmlparsedata_1.0.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xmlparsedata_1.0.5.tar.gz
Summary  : Parse Data of 'R' Code as an 'XML' Tree
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
tree, that one can search via 'XPath', and easier to manipulate in
    general.

%prep
%setup -q -c -n xmlparsedata
cd %{_builddir}/xmlparsedata

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615221147

%install
export SOURCE_DATE_EPOCH=1615221147
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xmlparsedata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xmlparsedata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xmlparsedata
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc xmlparsedata || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/xmlparsedata/DESCRIPTION
/usr/lib64/R/library/xmlparsedata/INDEX
/usr/lib64/R/library/xmlparsedata/LICENSE
/usr/lib64/R/library/xmlparsedata/Meta/Rd.rds
/usr/lib64/R/library/xmlparsedata/Meta/features.rds
/usr/lib64/R/library/xmlparsedata/Meta/hsearch.rds
/usr/lib64/R/library/xmlparsedata/Meta/links.rds
/usr/lib64/R/library/xmlparsedata/Meta/nsInfo.rds
/usr/lib64/R/library/xmlparsedata/Meta/package.rds
/usr/lib64/R/library/xmlparsedata/NAMESPACE
/usr/lib64/R/library/xmlparsedata/NEWS.md
/usr/lib64/R/library/xmlparsedata/R/xmlparsedata
/usr/lib64/R/library/xmlparsedata/R/xmlparsedata.rdb
/usr/lib64/R/library/xmlparsedata/R/xmlparsedata.rdx
/usr/lib64/R/library/xmlparsedata/help/AnIndex
/usr/lib64/R/library/xmlparsedata/help/aliases.rds
/usr/lib64/R/library/xmlparsedata/help/paths.rds
/usr/lib64/R/library/xmlparsedata/help/xmlparsedata.rdb
/usr/lib64/R/library/xmlparsedata/help/xmlparsedata.rdx
/usr/lib64/R/library/xmlparsedata/html/00Index.html
/usr/lib64/R/library/xmlparsedata/html/R.css
/usr/lib64/R/library/xmlparsedata/tests/testthat.R
/usr/lib64/R/library/xmlparsedata/tests/testthat/test.R
