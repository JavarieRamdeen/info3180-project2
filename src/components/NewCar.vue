<template>
<div class="create">
    <h1>Register New User</h1>
    <hr>
    <div class="form_container">
        <form class="d-flex flex-column justify-content-center">
            <label>Description</label>
            <div class="form-floating">
                <input v-model="description" type="text" class="form-control">
            </div>

            <label>Make</label>
            <div class="form-floating">
                <input v-model="make" type="password" class="form-control">
            </div>

            <label>Model</label>
            <div class="form-floating">
                <input v-model="model" type="text" class="form-control">
            </div>

            <label>Colour</label>
            <div class="form-floating">
                <input v-model="colour" type="email" class="form-control">
            </div>

            <label>Year</label>
            <div class="form-floating">
                <input v-model="Year" type="text" class="form-control">
            </div>

            <label>Transmission</label>
            <div class="form-floating">
                <input v-model="transmission" type="text" class="form-control">
            </div>

            <label>Car Type</label>
            <div class="form-floating">
                <input v-model="car_type" type="text" class="form-control">
            </div>

            <label>Price</label>
            <div class="form-floating">
                <input v-model="Price" type="text" class="form-control">
            </div>

            <label for="photo">Photo</label>
            <div class="form-floating">
                <input v-on:change="photo" type="file" id="Image" name="Image">
            </div>

            <button v-on:click="submit" class="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
          </form>
    </div>
</div>
 </template>

<script>
</script>

<style>
</style>