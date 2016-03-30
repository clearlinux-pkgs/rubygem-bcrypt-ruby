#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-bcrypt-ruby
Version  : 3.1.5
Release  : 4
URL      : https://rubygems.org/downloads/bcrypt-ruby-3.1.5.gem
Source0  : https://rubygems.org/downloads/bcrypt-ruby-3.1.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bcrypt
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec

%description
# bcrypt-ruby
An easy way to keep your users' passwords secure.
* http://github.com/codahale/bcrypt-ruby/tree/master

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n bcrypt-ruby-3.1.5
gem spec %{SOURCE0} -l --ruby > rubygem-bcrypt-ruby.gemspec

%build
gem build rubygem-bcrypt-ruby.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
bcrypt-ruby-3.1.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/bcrypt-ruby-3.1.5.gem
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-ruby-3.1.5/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-ruby-3.1.5/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-ruby-3.1.5/README.md
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-ruby-3.1.5/lib/bcrypt/dummy.rb
/usr/lib64/ruby/gems/2.3.0/specifications/bcrypt-ruby-3.1.5.gemspec
