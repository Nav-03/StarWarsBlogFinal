import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext.js";

export const Navbar = (props) => {
	const { store, actions } = useContext(Context);
	const session = actions.getCurrentSession();
	return (
		<nav className="navbar navbar-light bg-light mb-3">
			<Link to="/">
				<span className="navbar-brand mb-0 ms-3 h1">
					<img
						height="70"
						width="125"
						src="https://www.citypng.com/public/uploads/preview/-51608494584ia2sfbncsd.png"
					></img>
				</span>
			</Link>
			{session ?
				<button onClick={() => actions.clearSession()}>Log Out</button> :
				<Link to="/login">
					<button>Log me in!</button>
				</Link>}

			<div className="dropdown">
				<button
					className="btn btn-primary dropdown-toggle me-5"
					id="dropdownMenu2"
					data-toggle="dropdown"
					aria-expanded="false"
					data-bs-toggle="dropdown"
				>
					Favorites{" "}
					<span className="badge bg-secondary">{store.favorites.length}</span>
				</button>
				<div className="dropdown-menu" aria-labelledby="dropdownMenu2">
					<ul id="favoritelist">
						{store.favorites.length === 0 ? (
							<li className="list-group-item-action dropdown-item">(empty)</li>
						) : (
							store.favorites.map((f, i) => {
								const fav = f.character ? f.character : f.planet;
								const type = f.character ? "character" : "planet";
								return (
									<li
										className="list-group-item-action dropdown-item list-items"
										key={i}
									>
										<Link to={type + "/" + fav.id}>{fav.name}</Link>{" "}
										<span
											className="favoriteDelete"
											onClick={() => actions.removeFavorites(i)}
										>
											<i className="fas fa-trash"></i>
										</span>
									</li>
								);
							})
						)}
					</ul>
				</div>
			</div>
		</nav>
	);
};
