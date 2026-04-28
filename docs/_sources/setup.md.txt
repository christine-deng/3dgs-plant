# Setup

## Hardware

All programs used in this project were run on a computer with the following specifications:

- PC: Alienware Aurora R16 (x64)
- Processor: Intel(R) Core(TM) i9-14900KF  3.20 GHz
- RAM: 64.0 GB
- GPU: NVIDIA GeForce RTX 4090

## Installing Nerfstudio

Our project builds on [Splatfacto](https://docs.nerf.studio/nerfology/methods/splat.html), [Nerfstudio](https://docs.nerf.studio/index.html)'s open-source Python implementation of 3DGS.

Follow the [installation guide](https://docs.nerf.studio/quickstart/installation.html) for your appropriate operating system. This project installed Nerfstudio using the Linux
installation on WSL.

## Data Preparation

Create a folder called `data` under the `nerfstudio` directory. In `data`, create a folder called `plant`, and a folder within `plant` named `source`.
Add all raw images of the plant to be used in training in the `source` folder. The folder structure should look as such:

```
📂.../ 
├──📂nerfstudio/ 
│   ├──📂data/
│   │	├──📂plant/
│   │	│	├──📂source/
│   │	│	│	├── 🖼️ <raw image 0>
│   │	│	│	├── 🖼️ <raw image 1>
│   │	│	│	│...
│   │   │...
│   │...
│...
```

Nerfstudio has a [built-in command](https://docs.nerf.studio/quickstart/custom_dataset.html) for processing images using [COLMAP](https://colmap.github.io/). COLMAP is a
Structure from motion (SfM) algorithm, we utilize COLMAP to process the input images to estimate shared camera intrinsics and orientations per frame. The algorithm then matches correspondences between features across image pairs to generate a sparse 3D point cloud. This pre-existing geometry allows Gaussians to initialize at the positions of the points.

Make sure COLMAP is installed with ``conda install -c conda-forge colmap``.

Enter the `plant` directory, and run Nerfstudio's image processor.

```
cd /home/<user>/nerfstudio/data/plant
```

```
ns-process-data images --data source --output-dir .
```

The folder should now look like this:
```
📂.../ 
├──📂nerfstudio/ 
│   ├──📂data/
│   │	├──📂plant/
│   │	│	├──📂source/
│   │	│	│	├── 🖼️ <raw image 0>
│   │	│	│	├── 🖼️ <raw image 1>
│   │	│	│	│...
│   │	│	├──📂colmap/
│   │	│	├──📂images/
│   │	│	├──📂images_2/
│   │	│	├──📂images_4/
│   │	│	├──📂images_8/
│   │	│	├──📄 sparse_pc.ply
│   │	│	├──📄 transforms.json
│   │   │...
│   │...
│...
```
- `colmap/` contains the raw SfM output, including camera poses and the sparse point cloud in COLMAP format.
- `sparse_pc.ply` is the sparse 3D point cloud visualized from the COLMAP reconstruction.
- `transforms.json` contains camera intrinsic and extrinsic values in Nerfstudio format.
- `images/` contains the processed source images in the correct orientation for training.
- `images_2/`, `images_4/`, `images_8/` are downscaled versions of `images/` at 1/2, 1/4, and 1/8 resolution, respectively, used during training.