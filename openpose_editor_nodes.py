import json


OpenposeJSON = dict


class LoadOpenposeJSONNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_str": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("POSE_KEYPOINT",)
    FUNCTION = "load_json"
    CATEGORY = "openpose"

    def load_json(self, json_str: str) -> tuple[OpenposeJSON]:
        empty_pose = { "people": [], "canvas_width": 512, "canvas_height": 768 }
        return (json.loads(json_str.replace("'", '"') or "{}") or empty_pose,)
