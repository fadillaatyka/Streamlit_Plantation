import os
import torch
# Import your pipeline and video export methods here

def set_output_folder(folder_name="generated_videos") -> str:
    base_path = "/content/drive/My Drive"  # Adjust this if not using Google Drive
    output_folder = os.path.join(base_path, folder_name)
    os.makedirs(output_folder, exist_ok=True)
    return output_folder

def generate_video_from_caption(caption: str, output_folder: str) -> str:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_name = "generated_video"
    video = pipe(
        prompt=caption, 
        guidance_scale=6, 
        use_dynamic_cfg=True, 
        num_inference_steps=50, 
        height=512, 
        width=512
    ).frames[0]

    output_path = os.path.join(output_folder, f"{video_name}.mp4")
    export_to_video(video, output_path, fps=8)

    torch.cuda.empty_cache()

    return output_path
