# frozen_string_literal: true

# Add run=dry to see shell @commands
# Example: rake prod run=dry

require 'English'
require 'rake'
require 'yaml'

@project = YAML.safe_load `tau project`
@base_dir = ENV['TAKELAGE_PROJECT_BASE_DIR'] || "/tmp/#{@project['name']}"

#####################################################################
# Variables

# The tasks will add shell commands to this empty global array
@commands = []

# Used by task :default and by function subtasks
@overview = ENV['overview'] == 'true'

# Used by function subtasks
@subtasks = ENV['subtasks'] || ''

#####################################################################
# Default task

task :default do
  sh "rake overview=#{@overview} --tasks", verbose: false
end

#####################################################################
# Add a subtasks block

def subtasks(scope)
  # show desciption? (no description creates hidden task)
  desc "Show subtasks of #{scope}" if @overview && !@subtasks.eql?(scope)

  # register task!
  task :tasks do
    sh "rake overview=true subtasks=#{scope} --tasks", verbose: false
  end

  # show subtasks?
  yield unless @overview && !@subtasks.eql?(scope)
end

#####################################################################
# Import Rakefiles from rake subfolders

Dir.glob('rake/**/Rakefile').each do |rakefile|
  import rakefile unless rakefile == 'rake/meta/Rakefile'
end

#####################################################################
# Import library files from rake subfolders

Dir.glob('rake/**/lib/*.rb').each do |libfile|
  load libfile
end

#####################################################################
# Final task

# Detect run=dry command line parameter
dry_run = ENV['run'] == 'dry'

# if Rakefile is invoked with run=dry
# then print commands
# else run commands
task :finally do
  @commands.each do |command|
    if dry_run
      puts command
    else
      begin
        sh command
      rescue RuntimeError
        # do not show backtrace
        exit 1
      end
    end
  end
end

# Run final task at exit
at_exit { Rake::Task[:finally].invoke if $ERROR_INFO.nil? }
#####################################################################
