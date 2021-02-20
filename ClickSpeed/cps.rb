#!/usr/bin/env ruby

require 'gosu'

class MainWindow < Gosu::Window
    def initialize()
        @time = @click = 0
        super 200, 150, false
    end

    def need_cursor?
        true
    end

    def update()
        if @click != 0
            @time += 1
            puts "\e[H\e[2J"
            puts ((@click * 60)/@time)
        end
    end

    def draw()
        #
    end

    def button_down(id)
        @click += 1 if id == Gosu::MS_LEFT
    end
end

MainWindow.new.show()
