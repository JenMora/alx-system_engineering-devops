# Fixes an error with a WordPress Website
exec { 'fix_wordpress_error':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => "test -f /var/www/html/wp-settings.php", # Ensures the file exists before running the command
}
