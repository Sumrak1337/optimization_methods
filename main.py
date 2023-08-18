import numpy as np
import matplotlib.pyplot as plt
import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig

from defaults import CONFIGS_ROOT, METHODS_ROOT, RESULTS_ROOT


@hydra.main(version_base=None, config_path='configs', config_name='config')
def main(cfg: DictConfig):
    for function in cfg.functions:
        convergence = []
        labels = []
        f = instantiate(function)
        for method in cfg.methods:
            m = instantiate(method, function=f)

            m.get_min()

            labels.append(m.prefix)
            acc = np.minimum.accumulate(m.history - f.f_min)
            convergence.append(-np.log10(np.clip(acc, 1e-16, np.inf)))

        plt.figure(figsize=(8, 5))
        plt.title(f.prefix)
        max_iteration = np.min([len(conv) for conv in convergence])
        for conv in convergence:
            plt.plot(conv[:max_iteration+1])
        plt.legend(labels=labels)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    import sys
    import os
    sys.argv.append(f'hydra.run.dir="{RESULTS_ROOT}"')
    os.environ['HYDRA_FULL_ERROR'] = '1'
    main()
