file "test.py" do {
  atomic_update  = "TrueClass, FalseClass"
  backup = "FalseClass, Integer"
  checksum = "String"
}

directory "var/www/testdomain.info/html" do {
  owner  = "arindoms"
  group  = "staff"
  mode   = "0755"
  action = "create"
}

directory "etc/apache2/sites-available/" do {
  owner  = "arindoms"
  group  = "staff"
  mode   = "0755"
  action = "create"
}


template "testdomain.info.conf" do {
  path = "etc/apache2/sites-available/"
}

template "index.html" do {
  path = "var/www/testdomain.info/html/"
}
