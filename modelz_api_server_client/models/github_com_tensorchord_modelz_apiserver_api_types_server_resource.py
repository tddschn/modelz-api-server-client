from enum import Enum


class GithubComTensorchordModelzApiserverApiTypesServerResource(str, Enum):
    CPU_4C_16G = "cpu-4c-16g"
    NVIDIA_ADA_L4_8C_32G = "nvidia-ada-l4-8c-32g"
    NVIDIA_AMPERE_A100_40G_12C_85G = "nvidia-ampere-a100-40g-12c-85g"
    NVIDIA_TESLA_T4_4C_16G = "nvidia-tesla-t4-4c-16g"

    def __str__(self) -> str:
        return str(self.value)
