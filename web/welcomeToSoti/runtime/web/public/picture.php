<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to SOTI</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="/index.php">Soti member</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/about.html">About us</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<div class="container mt-4">
    <select class="form-select" aria-label="Default select example" id="selectPicture" onchange="picture()">
        <option selected>보고 싶은 사진을 선택해주세요</option>
        <option value="1.png">졸라맨</option>
        <option value="2.png">soti</option>
        <option value="3.png">jalnik</option>
    </select>
</div>

<script>
    function picture() {
        const pictureName = document.getElementById('selectPicture').value;
        document.location.href=`./picture.php?picture=${pictureName}`;
        
    }
</script>

<?php
    ini_set( "display_errors", 0 );
    $picture = $_GET['picture'];
?>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-12 col-md-6">
            <img src="data:image/jpeg;base64, <?php echo base64_encode(file_get_contents($picture)); ?>" class="img-fluid" alt="Centered Image" width="300px" height="300px">
        </div>
    </div>
</div>

</script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
</body>
</html>
