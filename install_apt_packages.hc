package "systemctl" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "systemctl"
}

package "apache2" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "apache2"
}

package "php7.2" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "php7.2"
}

package "libapache2-mod-php7.2" do {
  os            = [ "debian", "ubuntu" ] 
  action        = "install"
  package       = "libapache2-mod-php7.2"
}
