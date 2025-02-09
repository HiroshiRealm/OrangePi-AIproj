from tools.i18n.i18n import I18nAuto
i18n = I18nAuto()
from GPT_SoVITS.inference_webui import change_gpt_weights, change_sovits_weights, get_tts_wav
from enum import StrEnum
import soundfile as sf

class Language(StrEnum):
    ZH = "中文"
    EN = "英文"
    JA = "日文"

def inference(ref_audio_path: str, prompt_text: str, prompt_language: Language, text: str, text_language: Language, output_path: str, cut: bool = False):
    change_gpt_weights(gpt_path=GPT_model_path)
    change_sovits_weights(sovits_path=SoVITS_model_path)

    result = get_tts_wav(
        ref_audio_path=ref_audio_path,
        prompt_text=prompt_text,
        prompt_language=i18n(str(prompt_language)),
        text=text,
        text_language=i18n(str(text_language)),
        how_to_cut=i18n("不切") if not cut else i18n("按标点符号切")
    )

    result = list(result)
    if result:
        last_sampling_rate, last_audio_data = result[-1]
        output_wav_path = output_path
        sf.write(output_wav_path, last_audio_data, last_sampling_rate)