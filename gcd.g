gcd := function(a, b)
	local c;
	while b <> 0 do
		c := b;
		b := a mod b;
		a := c;
	od;
	return c;
end;
