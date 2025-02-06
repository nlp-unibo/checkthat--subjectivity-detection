from pathlib import Path
import pandas as pd
import numpy as np


def main():
    annotators = 7
    annotators_per_sample = 3
    language = 'en'
    base_path: Path = Path('.', 'annotation', language).resolve()
    save_path: Path = Path('.', 'assignments', language).resolve()

    if not save_path.is_dir():
        save_path.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(base_path.joinpath('dataset.csv'))
    assignments = np.random.rand(df.shape[0], annotators).argpartition(annotators_per_sample, axis=1)[:, :annotators_per_sample]

    for ann_idx in range(annotators):
        ann_indexes = np.where(assignments == ann_idx)[0]
        ann_df = df.iloc[ann_indexes]
        ann_df['sampling_id'] = ann_indexes
        ann_df = ann_df[['sampling_id', 'article_id', 'sentence', 'label']]
        ann_df = ann_df.sample(frac=1.0)

        print(f'Annotator {ann_idx}. Samples {ann_df.shape[0]}.')
        ann_df.to_csv(save_path.joinpath(f'ann_{ann_idx}.csv'), index=False)


if __name__ == '__main__':
    main()
