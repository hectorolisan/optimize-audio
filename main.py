#!/usr/bin/env python3

import sys

from pathlib import Path
from pydub import AudioSegment

from decorators import handle_errors, print_styled

OUTPUT_DIR = Path("output")

@handle_errors("Error al optimizar el audio")
def optimize_audio(audio_file: str) -> None:
    """Optimiza el audio."""
    input_path = Path(audio_file)
    output_filename = input_path.stem + ".mp3"
    output_path = OUTPUT_DIR / output_filename
    OUTPUT_DIR.mkdir(exist_ok=True)

    audio = AudioSegment.from_file(audio_file)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)
    audio = audio.set_frame_rate(44100)
    audio = audio.normalize()

    audio.export(output_path, format="mp3")
    print_styled(
        message=f"✓ Audio optimizado guardado en: {output_path}\n",
        color="green"
    )

def main():
    """Función principal que maneja la ejecución del script."""
    if len(sys.argv) != 2:
        print_styled(
            message="Número de argumentos inválido\n",
            error_type="ValueError",
            color="red"
        )
        print_styled(
            message="📖 Uso: python main.py <audio_file>",
            color="cyan"
        )
        print_styled(
            message="📝 Ejemplo: python main.py audio.mp3",
            color="cyan"
        )
        sys.exit(1)

    audio_file: str = sys.argv[1]
    optimize_audio(audio_file=audio_file)

if __name__ == "__main__":
    main()
