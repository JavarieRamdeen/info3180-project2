<template>
<div class="create">
    <h1>Register New User</h1>
    <hr>
    <div class="form_container">
        <form class="d-flex flex-column justify-content-center">
            <label>Username</label>
            <div class="form-floating">
                <input v-model="username" type="text" class="form-control">
            </div>

            <label>Password</label>
            <div class="form-floating">
                <input v-model="password" type="password" class="form-control">
            </div>

            <label>Fullname</label>
            <div class="form-floating">
                <input v-model="fullname" type="text" class="form-control">
            </div>

            <label>Email</label>
            <div class="form-floating">
                <input v-model="email" type="email" class="form-control">
            </div>

            <label>Location</label>
            <div class="form-floating">
                <input v-model="location" type="text" class="form-control">
            </div>

            <label>Biography</label>
            <div class="form-floating">
                <input v-model="biography" type="text" class="form-control">
            </div>

            <label for="photo">Photo</label>
            <div class="form-floating">
                <input v-on:change="photo" type="file" id="Image" name="Image">
            </div>

            <button v-on:click="register" class="w-100 btn btn-lg btn-primary" type="submit">Register</button>
          </form>
    </div>
</div>
 </template>

<script>
    import axios from 'axios'
    export default{
    name: "Register",
    data(){
        return{
            username: '',
            password: '',
            fullname: '',
            email: '',
            location: '',
            biography: '',
            photo: ''
        }
    },
    methods:{
        async register(){
            let result = await axios.post("http://localhost:8080/api/register",{
            username: this.username,
            password: this.password,
            fullname: this.fullname,
            email: this.email,
            location: this.location,
            biography: this.biography,
            photo: this.photo,
            });
            console.log(result)
        }
    }
}
</script>

<style>
</style>