#!/usr/bin/env ruby
require 'gosu'

class Sprite_Image
    attr_accessor :image, :sprite_pos, :size, :direction, :pos_x, :pos_y
    def initialize(user_path, frames, direction)
        @image = Gosu::Image.new(user_path)
        @size = @image.width / frames
        @sprite_pos = 0
        @pos_x = @pos_y = 50
        @direction = direction
    end
end

#? changes pointer in the sprite image
def animate(media, limit)
    media.sprite_pos += media.size
    media.sprite_pos = 0 if media.sprite_pos >= limit || media.sprite_pos < 0
end

#? asks user for required information
def get_details()
    print("image path: ")
    user_path = gets.chomp()
    if File.exists?(user_path)
        
        frames = 0
        while frames <= 0
            print("Number of Frames: ")
            frames = gets.chomp.to_i()
        end

        print("Direction [v/h] : ")
        direction = gets.chomp()
        media = Sprite_Image.new(user_path, frames, direction)
        return media
    else
        puts("enter valid path")
        get_details()
    end
end

#? to animate image at the center of dashboard
def draw_postion(media, ratio)
    media.pos_x = (636 - (media.image.width * ratio))/2
    media.pos_y = (621 - (media.image.height * ratio))/2
end

class Animator < Gosu::Window
    def initialize()
        @media = get_details()
        if @media.direction == 'v' then @limit = @media.image.height  else @limit = @media.image.width ; end
        @ratio = @index = @refreshrate = 1
        super 950, 700, false
    end

    def needs_cursor?
        true
    end

    def update()
        @index += 1
        animate(@media, @limit) if @index % @refreshrate == 0
    end

    def draw()
        #* base and dashboard
        Gosu.draw_rect(0, 0, 950, 700, 0xff_121212, 0)
        Gosu.draw_rect(29, 40, 636, 621, 0xff_232323, 0)

        for i in 1..4
            x, y = 680, 243
            y = 365 if i > 2
            x = 803 if i % 2 == 0
            Gosu.draw_rect(x, y, 100, 33, 0xff_e23f52, 1)
        end
        (Gosu::Font.new(65)).draw_text("animator", 690, 97, 1, 1.0, 1.0, 0xff_ffffff)
        (Gosu::Font.new(25)).draw_text("s p e e d", 745, 213, 1, 1.0, 1.0, 0xff_ffffff)
        (Gosu::Font.new(25)).draw_text("s i z e", 760, 335, 1, 1.0, 1.0, 0xff_fffffff)

        (Gosu::Font.new(25)).draw_text("FPS: #{60/@refreshrate}", 680, 635, 1, 1.0, 1.0, 0xff_fffffff)

        #draw_postion(@media, @ratio)
        @media.image.subimage(@media.sprite_pos, 0, @media.size, @media.image.height).draw(@media.pos_x, @media.pos_y, 1, @ratio, @ratio) if @media.direction == "v"
        @media.image.subimage(0, @media.sprite_pos, @media.image.width, @media.size).draw(@media.pos_x, @media.pos_y, 1, @ratio, @ratio) if @media.direction == "h"
    end

    def button_down(id)
        case id
        when Gosu::KB_ESCAPE
            close
        when Gosu::MS_LEFT
            if (680..780).include?(mouse_x) && (243..276).include?(mouse_y)
                @refreshrate += 1
            elsif (803..903).include?(mouse_x) && (243..276).include?(mouse_y)
                if (@refreshrate > 1) then @refreshrate -= 1 else puts("max"); end
            elsif (680..780).include?(mouse_x) && (365..398).include?(mouse_y)
                @ratio -= 1 if ((@media.image.width * @ratio) > -636) && ((@media.image.height * @ratio) > -620)
            elsif (803..903).include?(mouse_x) && (365..398).include?(mouse_y)
                @ratio += 1 if ((@media.image.width * @ratio) < 636) && ((@media.image.height * @ratio) < 620)
            end
        end
    end
end

Animator.new.show()
