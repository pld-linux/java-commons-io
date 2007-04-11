Summary:	Jakarta Commons IO component for Java servlets
Summary(pl.UTF-8):	Komponent Jakarta Commons IO dla serwletów Javy
Name:		jakarta-commons-io
Version:	1.3.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/io/source/commons-io-%{version}-src.tar.gz
# Source0-md5:	d003445638bc272512112ace08d63bbb
URL:		http://jakarta.apache.org/commons/io/
BuildRequires:	ant-junit >= 1.5
BuildRequires:	jakarta-servletapi >= 2.3
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.8.1
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Commons IO is a library of utilities to assist with developing
IO functionality.

%package doc
Summary:	Jakarta Commons IO documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons IO
Group:		Development/Languages/Java

%description doc
Jakarta Commons IO documentation.

%description doc -l pl.UTF-8
Dokumentacja do Jakarta Commons IO.

%prep
%setup -q -n commons-io-%{version}

%build
export JAVA_HOME="%{java_home}"
# for tests
export CLASSPATH="`build-classpath servlet junit`"
ant dist \
	-Dnoget=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-io-1.3.1-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/commons-io.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
