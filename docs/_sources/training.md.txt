# Training

## Nerfstudio Viewer
Now that we have the geometry of the scene from COLMAP and the segmentation masks, we can train the 3DGS model to optimize each Gaussian's position, color, opacity, and scale.

```
python -m nerfstudio.scripts.train splatfacto \
  --data /home/<user>/nerfstudio/data/plant \
  --vis viewer
```

The `masks` folder should be automatically detected by Nerfstudio. If not, include `--masks-path masks` in the command.

Training can be monitored in real-time via Nerfstudio's [web-based viewer](https://docs.nerf.studio/quickstart/viewer_quickstart.html). The above command will start a server and include the link in the terminal, it will typically look something like `http://localhost:7007`. Follow the link to visualize the training iterations.

## Output

The trained model is saved to the following directory:
```
📂.../
├──📂nerfstudio/
│   ├──📂outputs/
│   │   ├──📂unnamed/
│   │   │   ├──📂splatfacto/
│   │   │   │   ├──📂<timestamp>/
│   │   │   │   │   ├──📂nerfstudio_models/
│   │   │   │   │   │   ├──📄 step-000029999.ckpt
│   │   │   │   │   ├──📄 config.yml
│   │   │   │   │   ├──📄 dataparser_transforms.json
│   │   │   │   │   │...
│   │   │   │   │...
│   │   │   │...
│   │   │...
│   │...
│...
```
- `step-000029999.ckpt` is a checkpoint file saved at the final training step (29999). This file contains all optimized Gaussian parameters, including:
  - `means` — 3D position of each Gaussian in the scene
  - `scales` — size of each Gaussian along each axis
  - `quats` — rotation of each Gaussian
  - `features_dc` — base color of each Gaussian
  - `features_rest` — view-dependent color component
  - `opacities` — opacity of each Gaussian
- `config.yml` contains the full training configuration, such as the hyperparameters used.
- `dataparser_transforms.json` contains the scene scale and orientation transforms applied during training.