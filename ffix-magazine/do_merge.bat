@echo off
cd /d C:\Users\Stella\Desktop\ffix-magazine\parts
copy /b f01_head.html+02_overview.html+03_development.html+04_world.html+05_characters_a.html+05b_characters_b.html+06_story_a.html+06b_story_b.html+07_systems.html+07b_systems_b.html+08_review.html+09_gallery.html+f99_footer.html ..\index.html
for %%A in (..\index.html) do echo Size: %%~zA bytes
echo DONE
