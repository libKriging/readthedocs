(SecUpdate)=
# Update model objects and simulations

- $\Old{\m{X}}$: contains $\Old{n}$ observed or "old" design
  points. The corresponding observations $\Old{\m{y}}$ are known.

- $\New{\m{X}}$: contains $\New{n}$ "new" design points at which a prediction or
  a simulation is made. The corresponding vector of observations
  $\New{\m{y}}$ is unknown.

- $\Upd{\m{X}}$: contains $\Upd{n}$ "update" design points. The
  corresponding vector of observations $\Upd{\m{y}}$ is unknown.




- Updating a Kriging model object $\OldUpd{\m{X}}$

- Updating simulations 


## The Kriging weights

For all Kriging models the prediction is linear w.r.t. to the observations
and takes the form

$$ 
  \widehat{\m{y}}_{\tnew\vert\told} = \m{W}(\New{\m{X}} \vert \Old{\m{X}}) \,
  \Old{\m{y}} 
$$

where  $\m{W}(\New{\m{X}} \vert \Old{\m{X}})$ is a $\New{n} \times \Old{n}$ 
matrix of *Kriging Weights*. In this notation, the pipe $\vert$ does not stand for
conditioning since $\Old{\m{X}}$  and $\New{\m{X}}$ 
are not random. Yet the notation recalls
that the Kriging Weights depend on the two designs, keeping these in the
same order as our notations for conditioning. Also, it emphasizes the fact
that the matrix is a function of the two design matrices and does not
depend on the GP values.

The matrix of Kriging weights is given by

$$
  \m{W}(\New{\m{X}} \vert \Old{\m{X}}) = \NewOld{\m{C}} \OldOld{\m{C}}^{-1} 
$$

in the SK case and by 

$$
  \m{W}(\New{\m{X}} \vert \Old{\m{X}}) = 
  \left\{ \NewOld{\m{C}} + 
  \left[ \New{\m{F}} - \widehat{\m{F}}_{\tnew\vert\told}
  \right] \Cov(\widehat{\bs{\beta}}) \, \Old{\m{F}}^\top
  \right\} \OldOld{\m{C}}^{-1} 
$$
in the UK case, where $\widehat{\m{F}}_{\tnew\vert\told}$ is the SK
prediction of $\New{\m{F}}:=\m{f}(\New{\m{X}})$ given the observations
$\Old{\m{F}}$.

## Updating simulations

### Update non-conditional simulations: residual Kriging

Suppose first that we have a Simple Kriging model (with no trend) and
that we have performed a non-conditional simulation for a design with
two parts $\Upd{\m{X}}$ and $\New{\m{X}}$. The $m$ simulated paths are
stored in matrices $\m{Y}^{\texttt{sim}}_{\tupd}$ and
$\m{Y}^{\texttt{sim}}_{\tnew}$ with dimensions $\Upd{n} \times m$ 
and $\New{n} \times m$.

![](./tikzFigures/Fig4.png)

If at some point the vector $\Upd{\m{y}}$ of observations becomes
available, we can turn the non-conditional simulations in
$\m{Y}^{\texttt{sim}}_{\tnew}$ into conditional ones, say
$\m{Y}^{\texttt{sim}}_{\tnew\vert\tupd}$. In the vocabulary of data
assimilation we may say that we are updating the simulations
$\m{Y}^{\texttt{sim}}_{\tnew}$ by assimilating the observations
$\Upd{\m{y}}$. 

We can indeed obtain the conditional simulations using

$$
\m{Y}^{\texttt{sim}}_{\tnew \vert \tupd}[ \: ,\, j] := 
\m{Y}^{\texttt{sim}}_{\tnew}[\:,\, j] +  
\m{W}(\New{\m{X}} \vert \Upd{\m{X}}) \left\{\Upd{\m{y}} - 
\m{Y}^{\texttt{sim}}_{\tupd}[\:,\, j] \right\} \qquad j=1,\, \dots,\, m.
$$

The vector $\Upd{\m{y}} - \m{Y}^{\texttt{sim}}_{\tupd}[\:,\, j]$ which
may be called a "residual" can be stored as the column $j$ of a $\Upd{n} \times m$ matrix 
$\Upd{\m{Z}}$.

![](./tikzFigures/Fig5.png)

In the case where an Universal Kriging model is used, one can not
obtain non-conditional simulations because the unconditional
distribution of $\m{y}$ is improper. However the residual Kriging can
be used conditionally on observations $\Old{\m{y}}$ corresponding to a
design $\Old{\m{X}}$. 

### Update conditional situations: FOXY

Consider now the case where the simulation is conditional on
observations $\Old{\m{y}}$ corresponding to a design $\Old{\m{X}}$. We
can relax the no-trend assumption of the previous section and simply
assume but simply that the XXX.

![](./tikzFigures/Fig10.png)

Now suppose that the observations $\Upd{\m{y}}$ at some "update" design points
$\Upd{\m{X}}$ become available. We want to update the simulations 
$\m{Y}^{\texttt{sim}}_{\tnew \vert \told}$

![](./tikzFigures/Fig11.png)

For this aim we can use the Kriging residual algorithm above but *conditionally
on* $\Old{\m{y}}$.


$$
  \widetilde{C}(\m{x}, \, \m{x}') :=
  \Cov\{y(\m{x}),\, y(\m{x}') \, \vert\, \Old{\m{y}}\}.
$$
 
which is given by

$$
\begin{aligned}
\widetilde{C}(\m{x}, \, \m{x}')
	&= C(\m{x},\, \m{x}') -C(\m{x}, \,\m{X}_{\told}) \m{C}_{\told,\told}^{-1}\, 
C(\m{X}_{\told},\, \m{x}) \\
      &+ \left[\m{f}(\m{x}) 
- \widehat{\m{f}}(\m{x}) \right]^\top \Cov(\widehat{\bs{\beta}})
\left[\m{f}(\m{x}) 
- \widehat{\m{f}}(\m{x}) \right]
		\end{aligned}
$$
  
We need to have $\Upd{\m{X}}$
