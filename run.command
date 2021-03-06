dir_path=Downloads/den_downloader; 

python "${dir_path}/util/file_list_generator.py"; 

output_name=$(<Downloads/den_downloader/util/output_name.txt); 

ffmpeg -f "concat" -safe "0" -protocol_whitelist "file,http,https,tcp,tls" -i "${dir_path}/util/file_list.txt" -codec "copy" -bsf:a aac_adtstoasc "${dir_path}/${output_name}.mp4"