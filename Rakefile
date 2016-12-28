SERVICE = "sevasetu-mothercare"
REVISION = `git describe --always --dirty='-dirty'`.strip
BRANCH = `git symbolic-ref --short HEAD`.strip
IMAGE = "#{SERVICE}:#{BRANCH}"
IMAGE_WITH_REVISION = "#{IMAGE}-#{REVISION}"

task :build do |t|
  sh "docker build -t #{IMAGE_WITH_REVISION} ."
  puts "\e[32m \n\nImage: #{IMAGE_WITH_REVISION}\n\n\e[0m"
end

task :run => [:build] do |t|
  sh "docker run -d -p 8080:80 #{IMAGE_WITH_REVISION}"
  puts "\e[32m \n\n Booted up the container\n\n\e[0m"
end
