%lua_version %{lua: print(string.sub(_VERSION, 5))}

%lua_libdir %{_libdir}/lua/%{lua_version}
%lua_pkgdir %{_datadir}/lua/%{lua_version}

%lua_requires \
Requires: lua(abi) = %{lua_version} \
%{nil}

