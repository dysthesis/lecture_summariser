{
  inputs,
  pkgs,
  ...
}: let
  pkgs' = import inputs.nixpkgs {
    inherit (pkgs) system;
    config = {
      rocmSupport = true;
      allowUnfree = true;
    };
  };
in
  pkgs'.mkShell {
    name = "lecture_summariser";

    packages = with pkgs'; [
      nixd
      alejandra
      statix
      deadnix
      ffmpeg
      basedpyright
      black
      (openai-whisper.override {
        triton = null;
      })
      (python3.withPackages (
        p:
          with p; [
            (openai-whisper.override {
              triton = null;
            })
            pymupdf
            ollama
            transformers
            google-genai
            python-magic
          ]
      ))
    ];
    PYTORCH_ROCM_ARCH = "gfx1030";
    HSA_OVERRIDE_GFX_VERSION = "10.3.0";
    HCC_AMDGPU_TARGET = "gfx1030";
  }
