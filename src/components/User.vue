<template>
<div class="profile_card">
    <div class="profile_wrap">
        <div class="profile_img">
            <img src='' alt="profile_img">
            <p class="name">Javarie Ramdeen</p>
            <p class="username">@JRamdeen</p>
            <p class="description"></p>
            <p class="Email">Email: </p>
            <p class="location">Location: </p>
            <p class="date_join">Joined: {{ join }}</p>
        </div>
    </div>
    <div>
        <h2>Cars Favourited</h2>
    </div>
</div>
 </template>

<script>
</script>

<style>
.profile_wrap{
    padding: 50px 25px;
    background: blue;
    position: relative;
    text-align: center;
    color: white;
}

.profile_img img{
    width: 200px;
    border-radius: 50%
}

.profile_img .name{
    font-size:24px;
    font-weight: 500;
    margin:0;
}

.profile_img .username{
    font-size:18px;
    font-weight: 300;
    margin:0;
}

.profile_img .location{
    font-size:18px;
    font-weight: 300;
    margin:0;
}
.profile_img .date_join{
    font-size:18px;
    font-weight: 300;
    margin:0;
}

</style>