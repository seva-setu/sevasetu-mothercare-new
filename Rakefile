SERVICE = "sevasetu-mothercare"
REVISION = `git describe --always --dirty='-dirty'`.strip
BRANCH = `git symbolic-ref --short HEAD`.strip
IMAGE = "#{SERVICE}:#{BRANCH}"
IMAGE_WITH_REVISION = "#{IMAGE}-#{REVISION}"

task :build do |t|
  sh "docker build -t #{IMAGE_WITH_REVISION} ."
  sh "docker tag #{IMAGE_WITH_REVISION} #{IMAGE}"
end
